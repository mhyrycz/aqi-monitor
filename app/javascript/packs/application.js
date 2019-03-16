import ReactDOM from 'react-dom';
import React from 'react';
import AppRouter from './Router.js'

var componentRequireContext = require.context("components", true)
var ReactRailsUJS = require("react_ujs")
ReactRailsUJS.useContext(componentRequireContext)

ReactDOM.render(<AppRouter/>, document.getElementById('app'));
