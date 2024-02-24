# OPS-SAT UHF COM
## RX
The `rx` directory includes services that can be used to receive and display CSP packets sent by OPS-SAT-1.

#### /rx/receiver
A gnuradio script to receive AX.25 frames.

#### /rx/processor
A python script that will decode the received AX.25 frames and save the CSP frames into a Mongo database.

#### /rx/api
A REST-API server that provides an API to fetch all received frames.

#### rx/dashboard
The dashboard that displays the frames.




