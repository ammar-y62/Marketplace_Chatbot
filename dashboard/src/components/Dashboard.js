// src/components/Dashboard.js

import React, { useEffect, useState } from 'react';
import { fetchUnansweredQueries } from '../api/api';
import Table from './Table';
import SaveScriptForm from './SaveScriptForm';

const Dashboard = () => {
    const [queries, setQueries] = useState([]);

    // Fetch data when component loads
    useEffect(() => {
        const getQueries = async () => {
            try {
                const data = await fetchUnansweredQueries();
                setQueries(data);
            } catch (error) {
                console.error('Error fetching unanswered queries:', error);
            }
        };

        getQueries();
    }, []);

    const handleRespond = (row) => {
        alert(`Responding to query: ${row.message}`);
    };

    // Define table columns
    const columns = [
        { header: 'ID', key: 'id' },
        { header: 'Message', key: 'message' },
        { header: 'Timestamp', key: 'timestamp' },
    ];

    // Define actions for table
    const actions = [{ label: 'Respond', onClick: handleRespond }];

    return (
        <div className="container mt-5">
            <h1>Unanswered Queries</h1>
            <Table columns={columns} data={queries} actions={actions} />
            <SaveScriptForm />
        </div>
    );
};

export default Dashboard;
