import React from "react";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";

const MyNavbar = () => {
  return (
    <>
      <Navbar>
        <Navbar.Brand>
          <Link to="/" className="text-decoration-none text-black">Home</Link>
        </Navbar.Brand>
        <Container fluid>
          <Row>
            <Col>
              <Link to="/Characters" className="text-decoration-none text-black">Characters</Link>
            </Col>
            <Col>
              <Link to="/Episodes/" className="text-decoration-none text-black">Episodes</Link>
            </Col>
            <Col>
              <Link to="/Locations/" className="text-decoration-none text-black">Locations</Link>
            </Col>
            <Col>
              <Link to="/Favorites/" className="text-decoration-none text-black">Favorites</Link>
            </Col>
          </Row>
        </Container>
      </Navbar>
    </>
  );
};

export default MyNavbar;
