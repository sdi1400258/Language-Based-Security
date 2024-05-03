dating-server:
	$(TROUPE)/bin/troupec dating-server.trp -o ./out/dating-server.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-server.js --id=../ids/id-server.json --trustmap=../trustmaps/GoT.json --aliases=aliases.json

dating-client-alice:
	$(TROUPE)/bin/troupec dating-client-alice.trp -o ./out/dating-client.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client.js --id=../ids/id-client-alice.json --trustmap=../trustmaps/client.json

dating-client-bob:
	$(TROUPE)/bin/troupec dating-client-bob.trp -o ./out/dating-client.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client.js --id=../ids/id-client-bob.json --trustmap=../trustmaps/client.json