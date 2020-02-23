const { app, BrowserWindow } = require('electron')
const Communicator = require("./comms.js.js.js")
const comms = new Communicator()


function createWindow (width, height, source_path) {
	// Create the browser window.
	let win = new BrowserWindow({
		width: width || 1300,
		height: height || 700,
		webPreferences: {
			nodeIntegration: true
		}
	})

	win.loadFile(source_path || 'index.html')
	// win.webContents.openDevTools()

  // Emitted when the window is closed.
	win.on('closed', () => {
		// Dereference the window object, usually you would store windows
		// in an array if your app supports multi windows, this is the time
		// when you should delete the corresponding element.
		win = null
	})
}

app.on('window-all-closed', () => {
    console.log("Electron exit!!!")
    app.quit()
})

process.on("SIGINT", ()=>{
    console.log("Electron exit!!!")
	comms.quit()
    app.quit()
})


comms.on("new-window", (msg)=>{
    createWindow(msg.width, msg.height, msg.source_path)
})


app.on('ready', ()=>{
    comms.createPipe()
})