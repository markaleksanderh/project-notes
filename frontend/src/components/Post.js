import React, { Component } from 'react'

class Post extends Component {
  render() {
    return (
      <div>
        <h3>{this.props.post.node.title}</h3>
        <p>{this.props.post.node.body}</p>
      </div>
    )
  }
}

export default Post
