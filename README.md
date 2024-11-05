Once opened in an IDE, type "py manage.py runserver" in the terminal, making sure it is in the "...\GitHub\backbonejobapp2" folder.
For Mac users, type "python3 manage.py runserver".
Follow the link in the console to view the locally hosted website.

To view on separate devices (through VSCode):
1. Navigae to the "Ports" tab on the bottom of the VSCode window.
2. Select "Forward a Port" and enter "8000" as the port.
3. Take note of the host device's IPv4 address and add it to the "ALLOWED_HOSTS" list in "settings.py" of the "backbonejobapp2" folder.
4. In the terminal, type "py manage.py runserver <ip-address>:8000" (or "python3").
5. On the separate device's search engine, connected to the same network, enter the url "http://<ip-address>:8000".
