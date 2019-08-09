export default ({ req, redirect }) => {
  if (process.env.NODE_ENV === "production") {
    const protocol = req.protocol
    if (protocol === "http") {
      return redirect(301, `https://${req.headers.host}${req.url}`)
    }
  }
}
