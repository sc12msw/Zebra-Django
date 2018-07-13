# zebra-django

I had a lot of trouble with Zebra Broswer print so this is my alternative solution.

Print to zebra printers using the Django REST Framework

* Requires django rest framework and django 1.11

Install django server with django restframework on raspberry pi then also install cups

sudo -apt get install cups

sudo usermod -a -G lpadmin pi

sudo nano /etc/cups/cupsd.conf

Change Listen localhost:631 -> Port 631 To allow access to machines on the network

Add Allow @local access to server/admin pages and config

sudo /etc/init.d/cups restart to load changes

Navigate to [pi-ip]:631 you should now see the apple based printer server

Once set up configure your firewall on the raspberry pi to only allow requests from your website server and no where else using a ufw whitelist.

Add your printers using the django admin module and past in your ZPL using the {barcode} and {product} where you need the. For example:

`^XA

^FX Section with product name
^CF0,60
^FO220,50^FD{product}^FS
^CF0,40
^FO50,250^GB700,1,3^FS


^FX Section with barcode.
^BY5,2,270
^FO175,550^BC^FD{barcode}^FS


^XZ`

Then use your webapp to post data to the /labelprint (from backend as it has to be your server ip)
Example in wordpress:


`//Url of remote print server (white list policy will only accept if this is running on an accepted host)
$url = 'http://127.0.0.1/labelprint';
      $response = wp_remote_post($url , array(
    	'method'      => 'POST',
    	'timeout'     => 45,
    	'redirection' => 5,
    	'httpversion' => '1.0',
    	'blocking'    => true,

      'headers'     => array(
        'Authorization' => 'Token lotsofnumbersandsymbolsgohere',
        'Content-Type'  => 'application/json; charset=utf-8'
        ),

      'body'        => json_encode(array(
        'printer' => $printer,
        'barcode' => $barcode,
        'product' => $product
      )),

      'cookies'     => array()
        )
      );
`
