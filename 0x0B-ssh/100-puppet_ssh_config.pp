# Configures SSH to connect without a password
file_line { 'Turn off passwd auth' :
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => 'PasswordAuthentication',
  line   => 'PasswordAuthentication no'
}

file_line { 'Declare identity file' :
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton'
}
