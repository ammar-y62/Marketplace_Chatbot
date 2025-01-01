// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './components/Dashboard.js';
import ProductAnalysis from './components/ProductAnalysis';
import Marketing from './components/Marketing';
import Accomplishments from './components/Accomplishments.js';

function App() {
    return (
        <Router>
            <Header />
            <main className="content">
                <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/product-analysis" element={<ProductAnalysis />} />
                    <Route path="/marketing" element={<Marketing />} />
                    <Route path="/accomplishments" element={<Accomplishments />} />
                </Routes>
            </main>
            <Footer />
        </Router>
    );
}

export default App;
