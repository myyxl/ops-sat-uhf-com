import { AX25Header } from './AX25';
import { CSP1Header } from './CSP1';
import { SPPHeader } from './SPP';

export interface NanoComAX100Frame {
    header: {
        ax25: AX25Header;
        csp1: CSP1Header;
        spp: SPPHeader;
    };
    data: number[];
    raw: number[];
}
