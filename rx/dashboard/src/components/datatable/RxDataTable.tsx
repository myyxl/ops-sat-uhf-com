import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
import { RxDataTableRow } from './RxDataTableRow';

export const RxDataTable = () => {
    return (
        <TableContainer sx={{ borderRadius: '10px', boxShadow: '0px 0px 24px -1px rgba(0,0,0,0.18)' }}>
            <Table sx={{ minWidth: 650 }}>
                <TableHead sx={{ backgroundColor: '#ECECEC' }}>
                    <TableRow>
                        <TableCell sx={{ fontWeight: 'bold' }}>Time Received</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Source Component</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Source Port</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Size</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Details</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    <RxDataTableRow />
                    <RxDataTableRow />
                    <RxDataTableRow />
                </TableBody>
            </Table>
        </TableContainer>
    );
};
