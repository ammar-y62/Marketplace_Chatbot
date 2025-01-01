// src/components/Footer.js
import React from 'react';

const Footer = () => {
    return (
        <footer className="footer">
            <p>© {new Date().getFullYear()} Ammart. All Rights Reserved.</p>
            {/* <p>Contact us at: support@ammart.com</p> */}
        </footer>
    );
};

export default Footer;
