import React from 'react';
import { TableCell, TableRow } from '@mui/material';
import { OpenInNew } from '@mui/icons-material';

export const RxDataTableRow = () => {
    // '#F6F6F6'
    return (
        <TableRow key={'A'} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
            <TableCell>{'24.02.2024 14:00 '}</TableCell>
            <TableCell>{'NanoCom AX100 (#5)'}</TableCell>
            <TableCell>{'30'}</TableCell>
            <TableCell>{'170 Bytes'}</TableCell>
            <TableCell>
                <OpenInNew sx={{ cursor: 'pointer' }} />
            </TableCell>
        </TableRow>
    );
};
