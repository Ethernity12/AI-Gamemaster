import ChatContainer from "../../components/Chat/ChatContainer/ChatContainer";
import InputLine from "../../components/Chat/InputLine/InputLine";
import styles from './Chat.module.scss'

function Chat() {
    return (
        <div className={styles.chat}>
            <ChatContainer>
                <p>This is a simple chat interface.</p>
            </ChatContainer>
            <InputLine/>
        </div>
    )
}

export default Chat