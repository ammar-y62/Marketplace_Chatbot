// src/api.js
const BASE_URL = "http://127.0.0.1:5000";

export const fetchUnansweredQueries = async () => {
    const response = await fetch(`${BASE_URL}/api/get_unanswered`);
    return response.json();
};

export const saveScript = async (scriptContent) => {
    const response = await fetch(`${BASE_URL}/api/save_script`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ script: scriptContent }),
    });
    return response.json();
};
