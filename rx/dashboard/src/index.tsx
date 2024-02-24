import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { Dashboard } from './pages/Dashboard';
import { createMuiTheme, ThemeProvider } from '@mui/material';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

const theme = createMuiTheme({
    typography: {
        fontFamily: 'Inter',
    },
});

root.render(
    <React.StrictMode>
        <ThemeProvider theme={theme}>
            <Dashboard />
        </ThemeProvider>
    </React.StrictMode>,
);
