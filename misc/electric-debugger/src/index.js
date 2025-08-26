const { app, BrowserWindow, ipcMain, dialog } = require('electron')
const path = require('path');

const _ = ()=>{
  let p_ = [ 49, 51, 51, 55, 45 ];
  let p__ = [ 55, 51, 51, 49, 45 ];
  let p___ = [ 50, 48, 50, 53 ];
  let p____ = [ 45, 48, 50, 51, 52 ];

  return String.fromCharCode(...(p_.concat(p__).concat(p___).concat(p____)))
}

ipcMain.handle("get-key", async (e)=>{
  return _();
})
ipcMain.handle("alert-error", async (e, {title, msg}) =>{
  dialog.showErrorBox(title, msg)
} )
ipcMain.handle("login", async (e, {key}) =>{

  // Nope and no!
  if(key!==_()){
    console.log("No bypasses please!");
    return;
  }

  createFlagWindow();

} )


const createFlagWindow = () => {
  const win = new BrowserWindow({
    width: 900,
    height: 450,
    webPreferences: {
      devTools : false,
      contextIsolation: false
    }
  })

  win.center();
  win.loadFile('./pages/flag.html')
  win.setMenuBarVisibility(false);
  win.setAutoHideMenuBar(true);

  return win;
}

const createLoadingWindow = () => {
  const win = new BrowserWindow({
    width: 500,
    height: 350,
    frame: false,
    resizable: false,     
    fullscreenable: false,
    titleBarStyle: 'hidden',
    webPreferences: {
      devTools : false,
      contextIsolation: false
    }
  })
  win.center();
  win.loadFile('./pages/index.html')

  return win;
}

const activateLicense = ()=>{
  const win = new BrowserWindow({
    width: 473,
    height: 274,
    resizable: false,
    fullscreenable: false,
    maximizable: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: true,
      devTools : true
    }
  })
  win.setMenuBarVisibility(false);
  win.setAutoHideMenuBar(true);
  win.loadFile('./pages/activation.html')

  return win;
}

app.whenReady().then(() => {
  let win1 = createLoadingWindow();

  setTimeout(()=>{
    win1.close();
    activateLicense();
  },6500);
})