import { Dialog, DialogContent, DialogTitle, Grid, Typography } from '@mui/material';
import React from 'react';
import { Close } from '@mui/icons-material';

export const DetailDialog = () => {
    return (
        <Dialog maxWidth={'lg'} open={true}>
            <DialogTitle sx={{ display: 'flex' }}>
                <Typography>Details</Typography>
                <Close sx={{ marginLeft: 'auto' }} />
            </DialogTitle>
            <DialogContent>
                <Grid container width="900px">
                    <Grid container item xs={6} direction="column" gap={2}>
                        <Grid item>
                            <Typography fontWeight="bold" fontSize={23}>
                                General Information
                            </Typography>
                            <Typography>
                                <strong>Source Component:</strong> NanoCom AX100 (#5)
                            </Typography>
                            <Typography>
                                <strong>Source Port:</strong> 30
                            </Typography>
                            <Typography>
                                <strong>Time Received:</strong> 24.02.2024 14:00
                            </Typography>
                            <Typography>
                                <strong>Size:</strong> 170 Bytes
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Typography fontWeight="bold" fontSize={23}>
                                AX.25 Header
                            </Typography>
                            <Typography>
                                <strong>Source:</strong> DP0OPS
                            </Typography>
                            <Typography>
                                <strong>Destination:</strong> DL0ESA
                            </Typography>
                            <Typography>
                                <strong>CTRL:</strong> 3
                            </Typography>
                            <Typography>
                                <strong>PID:</strong> 1
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Typography fontWeight="bold" fontSize={23}>
                                CSP Header
                            </Typography>
                            <Typography>
                                <strong>Source:</strong> 30 (Port: 1)
                            </Typography>
                            <Typography>
                                <strong>Destination:</strong> 10 (Port: 30)
                            </Typography>
                            <Typography>
                                <strong>XTEA:</strong> 0
                            </Typography>
                            <Typography>
                                <strong>HMAC:</strong> 1
                            </Typography>
                            <Typography>
                                <strong>CRC:</strong> 0
                            </Typography>
                        </Grid>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography fontWeight="bold" fontSize={23}>
                            Data
                        </Typography>
                        <pre
                            style={{
                                whiteSpace: 'pre-wrap',
                                backgroundColor: '#ECECEC',
                                padding: 8,
                                borderRadius: 5,
                                height: '80%',
                            }}
                        >
                            <code>
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                                AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA
                            </code>
                        </pre>
                    </Grid>
                </Grid>
            </DialogContent>
        </Dialog>
    );
};
