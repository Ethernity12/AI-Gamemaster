import styles from "./AppContainer.module.scss";

function AppContainer({ children }: { children: React.ReactNode }) {
  return (
    <div className={styles.appContainer}>
      {children}
    </div>
  )
}

export default AppContainer