# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "
    server {
        listen 80;
        root /var/www/html;
        index index.html;
        location / {
            # Return "Hello World!" on GET request to root
            if (\$request_method = GET) {
                return 200 'Hello World!';
            }
        }
        location /redirect_me {
            # Perform 301 redirect
            return 301 /;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Start and enable Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

