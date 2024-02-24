export interface AX25Header {
    source: string;
    destination: string;
    ctrl: number;
    pid: number;
}
