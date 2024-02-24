export interface CSP1Header {
    priority: number;
    source: number;
    destination: number;
    destinationPort: number;
    sourcePort: number;
    reserved: number;
    hmac: number;
    xtea: number;
    rdp: number;
    crc: number;
}