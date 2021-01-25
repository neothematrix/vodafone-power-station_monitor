# vodafone-power-station_monitor

A quick scraper to programmatically collect useful info from the Vodafone Power Station router webpage

You'll need Python 3.x with the selenium module installed, plus a valid chromedriver, I used [this](https://chromedriver.chromium.org/downloads)

The script will connect to your Vodafone Power Station router webpage using the provided ip, username and password and will return a JSON formatted output that can be easily parsed and used anywhere you need.

It should be easy enough to extend the script by adding additional pages to scrape.

The code is just "raw", there is no error checking or other exception handling.

If you find a nice way to replace the selenium module with a lighter "requests" module I'd be very grateful, I still haven't found a way to replicate the javascript code that performs the login, hence the need to emulate a full browser with selenium.

## Usage

python3 vps_mon.py 192.168.1.1 username password

## Sample output

```json
{"connection_status": "UP", "model_name": "MA5671A", "vendor_name": "HUAWEI", "hw_version": "", "gpon_serial_number": "xxx", "registration_id": "xxx", "gpon_status": "", "received_power": "-24.32", "transmit_power": "1.73", "temperature": "49", "bip_errors": "0", "fw_version": "", "inter_ip_address": "x.x.x.x", "inter_gateway": "x.x.x.x", "inter_primary_dns": "x.x.x.x", "inter_secondary_dns": "x.x.x.x", "inter_firewall": "601036", "inter_wan_ip_address": "x.x.x.x", "inter_ipv6_link_local_address": "N/A", "inter_ipv6_link_global_address": "N/A", "inter_ipv6_gateway": "N/A", "inter_ipv6_prefix_delegation": "N/A", "inter_ipv6_dns_address1": "N/A", "inter_ipv6_dns_address2": "", "lan_ip_network": "192.168.1.0/24", "lan_default_gateway": "192.168.1.1", "lan_mac_address": "x-x-x-x-x-x", "lan_dhcp_server": "601036", "lan_dhcpv6_server": "601036", "lan_router_advertisement": "601036", "lan_ipv6_default_gateway": "x::x:x:x:x", "lan_port1": "601045", "lan_port2": "601045", "lan_port3": "601045", "lan_port4": "601046", "lan_port1_speed": "100", "lan_port2_speed": "1000", "lan_port3_speed": "1000", "lan_port4_speed": "0", "wifi_status": "601036", "wifi_name": "Vodafone-x", "wifi_mac_address": "x-x-x-x-x-x", "wifi_security": "401027", "wifi_channel": "7", "wifi_bandwidth": "288.5", "wifi_status_5g": "601036", "wifi_name_5g": "Vodafone5GHz-x", "wifi_mac_address_5g": "x-x-x-x-x-x", "wifi_security_5g": "401027", "wifi_channel_5g": "36,40,44,48", "wifi_bandwidth_5g": "2166.5", "guest_wifi_status": "601037", "guest_wifi_name": "Vodafone-Guest", "guest_wifi_mac_addr": "x-x-x-x-x-x", "guest_wifi_security": "WPA2", "guest_wifi_ip": "192.168.5.1", "guest_wifi_dhcp_server": "601036", "guest_wifi_status_5g": "601037", "guest_wifi_name_5g": "Vodafone-Guest", "guest_wifi_mac_addr_5g": "x-x-x-x-x-x", "guest_wifi_security_5g": "WPA2", "vf_internet_key_online_since": "", "vf_internet_key_ip_addr": "0.0.0.0", "vf_internet_key_system": "0.0.0.0", "vf_internet_key_mode": "auto", "sys_serial_number": "xxx", "sys_firmware_version": "XS_3.7.04.06", "sys_bootloader_version": "4.0.1.0", "sys_hardware_version": "VOX30v1", "sys_uptime": "17:23:36:37", "sys_cpu_usage": "11.44%", "sys_reboot_cause": "PowerOff", "sys_memory_usage": "64.92%", "sys_wireless_driver_version": "7.35.260.93029 (r766613) FWID 01-7fc70ca8;10.10.131.36 (r766584) FWID 01-e9ce5124", "sys_date_time": "2021-01-25 22:48:55"}```
