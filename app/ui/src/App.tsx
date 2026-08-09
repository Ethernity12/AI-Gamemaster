import LenghtMeter from "./components/Chat/LenghtMeter/LenghtMeter"
import Chat from "./pages/Chat/Chat"
import Menu from "./components/Chat/Menu/Menu"
import AppContainer from "./components/Common/AppContainer"

function App() {
  return (
    <AppContainer>
      <Menu/>
      <Chat/>
      <LenghtMeter/>
    </AppContainer>
  )
}

export default App