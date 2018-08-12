<template>
	<div>
<!-- 		<div id="main" align="center">
			<form id="form" name="form" class="pure-form pure-form-stacked">
				<fieldset>
					<div class="pure-item">
						<label for="host">Host</label>
						<input id="host" name="host" type="text" placeholder="Host">
					</div>
					<div class="pure-item">
						<label for="port">Port</label>
						<input id="port" name="port" type="text" placeholder="Port">
					</div>
					<div class="pure-item">
						<label for="username">Username</label>
						<input id="username" name="username" type="text" placeholder="Username">
					</div>
					<div class="pure-item">
						<label>Type</label>
						<div id="ratio-group">
							<label for="password" class="pure-radio">
								<input id="password" type="radio" name="ispwd" value="true" checked>
								Password
							</label>
							<label for="primerykey" class="pure-radio">
								<input id="primerykey" type="radio" name="ispwd" value="false">
								Primary Key
							</label>
						</div>
					</div>
					<div class="pure-item">
						<label for="secret">Secret</label>
						<input id="secret" name="secret" type="password"
						placeholder="Password or Private Key">
					</div>
					<label for="remember" class="pure-checkbox">
						<input id="remember" type="checkbox"> Remember me
					</label>
					<button type="button" class="pure-button pure-button-primary" @click="connect()">Connect</button>
				</fieldset>
			</form>
		</div> -->
		<div id="term" align="center"></div>
	</div>
</template>

<script>

import $ from 'jquery'
import Terminal from './Xterm'
import WSSHClient from './ws'

export default {
	name: 'Terminal',
    props:['username','server'],
	data() {
		return {
			charWidth: 6.2,
			charHeight: 15.2
		}
	},
	mouted() {
		this.connect();
	},
	computed: {
		options() {
			return JSON.parse(this.server);
		}
	},
	methods: {
		openTerminal(options) {
		    if (!$.isEmptyObject($('.terminal')[0])){
		        alert("请先退出当前Terminal(CTRL+D或exit)")
		        return
		    }
		    var client = new WSSHClient();

		    var term = new Terminal({cols: 80, rows: 80, screenKeys: true, useStyle: true});
		    term.on('data', function (data) {
		        client.sendClientData(data);
		    });
		    term.open();
		    $('.terminal').detach().appendTo('#term');
		    $("#term").show();
		    term.write('Connecting...' + '\r\n');

		    client.connect({
		        onError: function (error) {
		            term.write('Error: ' + error + '\r\n');
		            console.debug('Error: '+error);
		            alert('Error: '+error)
		            term.destroy();
		        },
		        onConnect: function () {
		            client.sendInitData(options);
		            // client.sendClientData('\r');
		            console.debug('connection established');
		        },
		        onClose: function (e) {
		            term.write("\rconnection closed")
		            console.debug(e);
		            //document.getElementById('term').style.display="none";
		            term.destroy();
		        },
		        onData: function (data) {
		            term.write(data);
		            // console.debug('get data:' + data);
		        }
		    })

		},

		/**
		 * for full screen
		 * @returns { w: number, h: number }
		 */
		getTerminalSize() {
		    var width = window.innerWidth;
		    var height = window.innerHeight;
		    return {
		        w: Math.floor(width / charWidth),
		        h: Math.floor(height / charHeight)
		    };
		},


		store(options) {
		    window.localStorage.host = options.host
		    window.localStorage.port = options.port
		    window.localStorage.username = options.username
		    window.localStorage.ispwd = options.ispwd;
		    window.localStorage.secret = options.secret
		},

		connect() {
		    console.debug(this.options);
	        // this.store(this.options);
		    this.openTerminal(this.options);
		}
	}
}
</script>