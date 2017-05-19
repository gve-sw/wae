from WAEWrapper import WAEWrapper

myWAEObject = WAEWrapper()
myWAEObject.listPaths("198.18.134.26", "7777")
myWAEObject.createLSP("198.18.134.26", "7777", "tunnel-1", "rtp", "sjc")
myWAEObject.listPaths("198.18.134.26", "7777")
myWAEObject.modifyLSP("198.18.134.26", "7777", "tunnel-1", "node-1", "5", "3", "3")
myWAEObject.listPaths("198.18.134.26", "7777")
