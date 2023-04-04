# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure custom HTTP header for Nginx
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;

                index index.html index.htm index.nginx-debian.html;

                server_name _;

                location / {
                        proxy_set_header X-Served-By $hostname;
                        try_files $uri $uri/ =404;
                }
        }",
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled on boot
service { 'nginx':
  ensure => running,
  enable => true,
}
