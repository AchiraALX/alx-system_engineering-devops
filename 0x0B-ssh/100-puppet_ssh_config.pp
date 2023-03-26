# Set up SSH client configuration file using Puppet

# Declare the file resource to edit
file { '/home/vagrant/.ssh/config':
  # Make sure the file exists and has the correct permissions and ownership
  ensure => 'file',
  mode   => '0600',
  owner  => 'vagrant',
  group  => 'vagrant',
  # Add the necessary configuration lines to the file using file_line resources
  # Configure SSH to use the private key ~/.ssh/school
  # and to refuse to authenticate using a password
  content => "Host *\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}

# Add file_line resource to turn off password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'PasswordAuthentication no',
}

# Add file_line resource to declare the identity file
file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/vagrant/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
