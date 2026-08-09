import styles from './ChatContainer.module.scss'

function ChatContainer ({ children }: { children: React.ReactNode }) {
    return (
        <div className={styles.chatContainer}>
            {children}
        </div>
    )
}

export default ChatContainer