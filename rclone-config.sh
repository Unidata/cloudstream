#!/usr/bin/expect -f
spawn rclone config
expect "n/s/q> "
send "n\r"
expect "name> "
send "dropbox\r"
expect "Storage> "
send "4\r"

expect "app_key> "
send "\r"
expect "app_secret> "
send "\r"

# https://www.safaribooksonline.com/library/view/exploring-expect/9781565920903/ch04.html
expect "https://*code"
spawn "firefox $expect_out(buffer)"


expect "Enter the code: "
