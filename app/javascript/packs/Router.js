import React from "react";
import ReactDOM from "react-dom";
import styled from "styled-components";
import Chart from "../components/Chart"

const DashBoardBody = styled.div`
  width: 100%;
  height: 100vh;
  font-family: "Open Sans", sans-serif;
`;

class AppRouter extends React.Component {

  render() {
    return (
      <DashBoardBody>
        <Chart />
      </DashBoardBody>
    );
  }
}

export default AppRouter;
