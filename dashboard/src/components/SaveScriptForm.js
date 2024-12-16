// src/components/SaveScriptForm.js

import React, { useState } from 'react';
import { saveScript } from '../api/api';

const SaveScriptForm = () => {
    const [scriptContent, setScriptContent] = useState('');

    const handleSave = async () => {
        if (!scriptContent.trim()) {
            alert('Please enter script content before saving.');
            return;
        }

        try {
            const response = await saveScript(scriptContent);
            alert(response.status === 'success' ? 'Script saved successfully!' : 'Failed to save script.');
            setScriptContent('');
        } catch (error) {
            alert('Error saving script. Please try again.');
        }
    };

    return (
        <div className="mt-5">
            <h2>Save Script</h2>
            <textarea
                className="form-control mb-3"
                rows="3"
                value={scriptContent}
                onChange={(e) => setScriptContent(e.target.value)}
                placeholder="Type your script here..."
            ></textarea>
            <button className="btn btn-success" onClick={handleSave}>
                Save Script
            </button>
        </div>
    );
};

export default SaveScriptForm;
