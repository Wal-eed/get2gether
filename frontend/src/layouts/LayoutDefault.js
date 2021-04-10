import React, { useState } from 'react';
import Header from '../components/layout/Header';
import Footer from '../components/layout/Footer';

const LayoutDefault = ({ children }) => {
  const [username, setUsername] = useState("");

  const childrenWithProps = React.Children.map(children, child => {
    // checking isValidElement is the safe way and avoids a typescript error too
    if (React.isValidElement(child)) {
      return React.cloneElement(child, { username: username, setUsername: setUsername });
    }
    return child;
  });

  return (
    <>
      <Header username={username} navPosition="right" className="reveal-from-bottom" />
      <main className="site-content">
        {childrenWithProps}
      </main>
      <Footer />
    </>
  )
};

export default LayoutDefault;  