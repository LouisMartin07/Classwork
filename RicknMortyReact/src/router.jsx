import { createBrowserRouter } from "react-router-dom"
import App from "./App";
import AboutPage from "../pages/AboutPage";
import CharactersPage from "../pages/CharactersPage";
import EpisodesPage from "../pages/EpisodesPage";
import LocationsPage from "../pages/LocationsPage";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        children: [
            {
                index: true,
                element: <AboutPage/>
            },
            {
                path: "/Characters/",
                element: <CharactersPage/>
            },
            {
                path: "/Episodes/",
                element: <EpisodesPage/>
            },
            {
                path: "/Locations/",
                element: <LocationsPage/>
            },
        ],
    }
]);

export default router;