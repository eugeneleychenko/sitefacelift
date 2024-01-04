import AOS from "aos";
import "aos/dist/aos.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import { useEffect } from "react";
import Home from "./pages/Home";
import Landing from "./components/Landing/Landing";

function App() {
  useEffect(() => {
    AOS.init();
    AOS.refresh();
    // if (window.location.pathname === '/') {
    //   window.location.href = "https://diplomatic-camel-6l1cd.mystrikingly.com/";
    // }
  }, []);
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route element={<Home />} path="/:domain" />
      </Routes>
    </Router>
  );
}

export default App;
