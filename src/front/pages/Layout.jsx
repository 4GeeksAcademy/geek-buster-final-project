import { Outlet } from "react-router-dom/dist"
import ScrollToTop from "../components/ScrollToTop"
import { Navbar } from "../components/Navbar"
import { Footer } from "../components/Footer"
import useGlobalReducer from "../hooks/useGlobalReducer"

// Base component that maintains the navbar and footer throughout the page and the scroll to top functionality.
export const Layout = () => {
    const {store} = useGlobalReducer();
   
    return (
        <ScrollToTop>
            <Navbar isLoggedIn = {!!store.token} user = {store.user} /> 
                <Outlet />
            <Footer />
        </ScrollToTop>
    )
}