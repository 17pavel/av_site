import React, { useState } from 'react';
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import { SmartCaptcha } from '@yandex/smart-captcha';


const Signup = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isCaptchaVerified, setIsCaptchaVerified] = useState(false);

  const onChangeUsername = (e) => {
    const username = e.target.value;
    setUsername(username);
  };

  const onChangePassword = (e) => {
    const password = e.target.value;
    setPassword(password);
  };

  const onCaptchaVerify = () => {
    setIsCaptchaVerified(true);
  };

  const signup = () => {
    if (isCaptchaVerified) {
      props.signup({ username: username, password: password });
      props.history.push('/');
    } else {
      alert("Please verify that you are not a robot.");
    }
  }

  return (
    <Container>
      <Form>
        <Form.Group className="mb-3">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={onChangeUsername}
          />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={onChangePassword}
          />
        </Form.Group>
        <Button variant="primary" onClick={signup}>
          Sign Up
        </Button>
        <SmartCaptcha 
          sitekey="ysc1_Ze6cfDd8BRgnIXW8jwlxTLBWxOyi90maaU8gJ7dA467f7599"
          onSuccess={onCaptchaVerify} />
      </Form>
    </Container>
  );
};

export default Signup;
