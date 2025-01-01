// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css'; // For basic styling
import logo from '../assets/Logo.png';

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <img src={logo} alt="Ammart Logo" />
                <h1>Ammart</h1>
            </div>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/product-analysis">Product Analysis</Link></li>
                    <li><Link to="/marketing">Marketing</Link></li>
                    <li><Link to="/accomplishments">Accomplishments</Link></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
