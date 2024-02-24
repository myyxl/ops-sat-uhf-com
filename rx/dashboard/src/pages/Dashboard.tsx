import { Grid, Typography } from '@mui/material';
import React from 'react';
import { RxDataTable } from '../components/datatable/RxDataTable';

export const Dashboard = () => {
    return (
        <Grid container direction="column">
            <Grid item container justifyContent="center" xs={1}>
                <Typography fontWeight="bold" fontSize={45} marginTop={5} fontFamily={'Inter'}>
                    OPS-SAT UHF RX
                </Typography>
            </Grid>
            <Grid item xs={11} sx={{ padding: 8 }}>
                <RxDataTable />
            </Grid>
        </Grid>
    );
};
