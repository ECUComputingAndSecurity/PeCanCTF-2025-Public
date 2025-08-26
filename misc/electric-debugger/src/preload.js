const { contextBridge, ipcRenderer, webFrame } = require('electron');


webFrame.setZoomFactor(0.9)

contextBridge.exposeInMainWorld('electric_api', {
  getKey: () => ipcRenderer.invoke('get-key'),
  error: (title, msg) => ipcRenderer.invoke('alert-error', { title, msg }),
  login : (key) => ipcRenderer.invoke('login', { key })
});
