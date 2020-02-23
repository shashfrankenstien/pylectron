const net = require("net")

class Communicator {
    constructor() {
        this.createPipe = this.createPipe.bind(this)
        this.topics = {}
        this.server = null
    }

    createPipe() {
        let t = this
        this.server = net.createServer(function(sock) {
            console.log('CONNECTED: ' + sock.remoteAddress +':'+ sock.remotePort)

            sock.on('data', function(data) {
                console.log('DATA ' + sock.remoteAddress + ': ' + data)
                t.dispatcher(JSON.parse(data))
            })

            sock.on('close', function(data) {
                console.log('CLOSED: ' + sock.remoteAddress +' '+ sock.remotePort)
            })

        })
        this.server.listen(1234, "127.0.0.1")
    }

    on(topic, cb) {
        this.topics[topic] = cb
    }

    dispatcher(data) {
        if ((data.topic) && (this.topics[data.topic])) {
            this.topics[data.topic](data.msg)
        }
    }

    quit() {
        if (this.server) {
            this.server.close()
        }
    }
}

module.exports = Communicator
