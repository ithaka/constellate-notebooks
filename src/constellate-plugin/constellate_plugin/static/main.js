const config = {
  GoogleAnalytics: {
    trackingId: 'UA-125778965-3'
  },
  Session: {
    url: 'https://www.jstor.org/api/tdm/v1/session',
    refreshTimeout: 1200000, // 20 minutes
  },
  ConstellateApi: {
    url: 'https://backend.tdm-pilot.org'
  }
};

define([
    'base/js/namespace',
    'base/js/events'
  ],
  function(Jupyter, events) {
    let userSession = {};
    const PARAMETERS_MARKER = '# Parameters:';
    var set_parameters = function() {
      const cells = Jupyter.notebook.get_cells();
      var autorun = false;
      const searchParams = new URL(window.location.href).searchParams;
      const datasetId = searchParams.get("id");
      var replaced = false;
      if (datasetId) {
        for (var c = 0; c < cells.length; ++c) {
          var cellData = cells[c];
          if (cellData.cell_type === "code") {
            var contents = cellData.get_text();
            var lines = contents.split(/\r?\n/);
            for (l = 0; l < lines.length; l++) {
              const codeLine = lines[l];
              if (codeLine.startsWith("dataset_id")) {
                var newId = "dataset_id = \"" + datasetId + "\"";
                var newContents = contents.replace(codeLine, newId);
                cellData.set_text(newContents);
                cellData.code_mirror.addLineClass(l, "background", "codehighlighter");
                console.log("notebookparams: replaced " + codeLine + " with " + datasetId);
                replaced = true;
                break;
              }
            }
          }
          if (replaced != false) {
            break;
          }
        }
      }
      if (searchParams.get("autorun") == "true") {
        if (Jupyter.notebook.kernel && Jupyter.notebook.kernel.is_connected()) {
          console.log('notebookparams: kernel connected, autorun');
          Jupyter.notebook.execute_all_cells();
        }
        else {
          console.log('notebookparams: waiting for kernel_ready before autorun');
          events.on('kernel_ready.Kernel', function(event, data) {
            Jupyter.notebook.execute_all_cells();
          });
        }
      }
    };

    function initializeSession() {
      const url = config.Session.url;
      return fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        referrerPolicy: 'no-referrer',
      });
    }

    function refreshSession() {
      const { session } = userSession;
      const url = config.Session.url;
      if (session) {
        return fetch(`${url}/refresh`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          referrerPolicy: 'no-referrer',
          body: JSON.stringify({uuid: session.uuid})
        }).catch(() => initializeSession());
      }

      return initializeSession();
    }

    function logEvent(eventtype, data = {}) {
      const { session } = userSession;
      if (session) {
        const eventTypeMissing = !eventtype;
        if (eventTypeMissing) return;

        const body = {...data, eventtype};
        const url = `${config.ConstellateApi.url}/log`;
        fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `UUID ${session.uuid}`
          },
          referrerPolicy: 'no-referrer',
          body: JSON.stringify(body)
        }).then(async res => {
          const result = await res.json();
          console.log(result);
        });
      }
    }

    function initializeEventLogging() {
      const searchParams = new URL(window.location.href).searchParams;
      const dataset_id = searchParams.get("id");

      Jupyter.notebook.events.on('kernel_connected.Kernel', function (evt, data) {
        logEvent('notebook-kernel-connect', {
          notebook: Jupyter.notebook.notebook_name,
          kernel: data.kernel.name,
          dataset_id
        });
      });

      Jupyter.notebook.events.on('kernel_disconnected.Kernel', function (evt, data) {
        logEvent('notebook-kernel-disconnect', {
          notebook: Jupyter.notebook.notebook_name,
          kernel: data.kernel.name,
          dataset_id
        });
      });

      Jupyter.notebook.events.on('execute.CodeCell', function (evt, data) {
        logEvent('notebook-cell-execute', {
          notebook: data.cell.notebook.notebook_name,
          kernel: data.cell.kernel.name,
          dataset_id
        });
      });
    }

    function initializeGoogleAnalytics()  {
      /* Begin Google Analytics script init */
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', config.GoogleAnalytics.trackingId, 'auto');
      /* End Google Analytics script init */

      Jupyter.notebook.events.on('kernel_connected.Kernel', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'kernel_connected.Kernel',
          eventLabel: data.kernel.name,
        });
      });

      Jupyter.notebook.events.on('kernel_disconnected.Kernel', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'kernel_disconnected.Kernel',
          eventLabel: data.kernel.name,
        });
      });

      Jupyter.notebook.events.on('delete.Cell', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'delete.Cell',
          eventLabel: data.cell.notebook.notebook_name,
        });
      });

      Jupyter.notebook.events.on('create.Cell', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'create.Cell',
          eventLabel: data.cell.notebook.notebook_name,
        });
      });

      Jupyter.notebook.events.on('edit_mode.Cell', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'edit_mode.Cell',
          eventLabel: data.cell.notebook.notebook_name,
        });
      });

      Jupyter.notebook.events.on('execute.CodeCell', function (evt, data) {
        ga('send', {
          hitType: 'event',
          eventCategory: 'Notebook',
          eventAction: 'execute.CodeCell',
          eventLabel: data.cell.notebook.notebook_name,
        });
      });
    }

    // Run on start
    function load_ipython_extension() {
      var style = document.createElement('style');
      style.type = 'text/css';
      style.innerHTML = '.codehighlighter { background: yellow; }';
      document.getElementsByTagName('head')[0].appendChild(style);
      set_parameters();
      initializeGoogleAnalytics();
      refreshSession().then(async res => {
        userSession = await res.json();

        logEvent('notebook-session-create', {
          kernel: Jupyter.notebook.kernel.name,
          notebook: Jupyter.notebook.notebook_name
        });

        initializeEventLogging();
      });
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
