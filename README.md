# Python Jammer

This script represents an easy way to generate a Wifi Network Jammer with Python and other 3rd party tools. This performs a network selection and then sends packets with certain characteristics (check the `RadioTop` layer on 802.11 norms) and with `DeAuth` instructions against your router in order block internet connection to the whole network.

A good resource for understanding more about the `RadioTop` packet can be found [here](http://wifinigel.blogspot.com/2013/11/what-are-radiotap-headers.html):

## Setup

The network interface should be in `Monitor mode`. You will need to first, shutdown down for Wifi interface `iwconfig <iface> down`,  then change the configuration like ` iwconfig <iface> mode monitor`

Monitor mode: promiscuous mode

## How it works

This script internally creates a `wireless` object that will help us connect the program to a wireless network. Later, the `wifi` package presents a simple way of `iwconfig` CLI-based for listing network interfaces installed and also for accessing

## Usage

Simple, just: `python jammer.py`.

Check the `requirements.txt` for dependencies and also check for the `conf.iface` property inside the `jam` function, in order to change the hard-coded NIC set there.


## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
