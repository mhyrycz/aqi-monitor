import React, { Component } from 'react';
import './App.css';
import Chart from './Chart';

class App extends Component {
  constructor(){
    super();
    this.state = {
      chartData:{}
    }
  }

  componentWillMount(){
    this.getChartData();
  }

  getChartData(){
    // Ajax calls here
    this.setState({
      chartData:{
        labels: this.props.time_labels,
        datasets:[
          {
            label:'Current Air Status',
            data: this.props.aqi,
            borderColor: "rgba(0,0,255,0.8)",
            backgroundColor:"rgba(0,0,255,0.2)"
          }
        ]
      }
    });
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
        </div>
        <Chart chartData={this.state.chartData} height={'200'} location="Massachusetts" legendPosition="bottom"/>
      </div>
    );
  }
}

export default App;
