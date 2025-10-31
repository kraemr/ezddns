# Use-case
receive ddns requests and dynamically update ip-records of a Domain by calling into APi's etc.

# Why ?
The original impetus was me not wanting to rely on external sites to get my ip for my ddns setup, since my router already has ddns support altough with limited vendor support.
Instead the router sends the request containing ipv4,ipv6,hostname,username etc to this server, which then updates the actual records.
This has the benefit of running locally.

