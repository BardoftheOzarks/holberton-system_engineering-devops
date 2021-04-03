# Configures SSH to connect without a password
file { '/etc/ssh/sshd_config':
  ensure => present,
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/holberton',
}