import React from 'react';
import PropTypes from 'prop-types';
import './header.css';

export default class Header extends React.Component {
    constructor(props){
        super(props);
    }
    
    render() {
        return (
            <div className="header">
                <p>Header</p>
            </div>
        );
    }
}