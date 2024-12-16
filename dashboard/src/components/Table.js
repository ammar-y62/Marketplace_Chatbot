// src/components/Table.js

import React from 'react';

const Table = ({ columns, data, actions }) => {
    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    {columns.map((col, index) => (
                        <th key={index}>{col.header}</th>
                    ))}
                    {actions && <th>Actions</th>}
                </tr>
            </thead>
            <tbody>
                {data.map((row, rowIndex) => (
                    <tr key={rowIndex}>
                        {columns.map((col, colIndex) => (
                            <td key={colIndex}>{row[col.key]}</td>
                        ))}
                        {actions && (
                            <td>
                                {actions.map((action, actionIndex) => (
                                    <button
                                        key={actionIndex}
                                        className="btn btn-sm btn-primary"
                                        onClick={() => action.onClick(row)}
                                    >
                                        {action.label}
                                    </button>
                                ))}
                            </td>
                        )}
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default Table;
