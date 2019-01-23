import React, { Component } from 'react'

class Post extends Component {
  render() {
    return (
      <div>
        <h3>{this.props.post.node.title}</h3>
        <p>{this.props.post.node.body} <span>{this.props.post.node.id}, {this.props.post.node.uuid}</span></p>
      </div>
    )
  }
}

export default Post
