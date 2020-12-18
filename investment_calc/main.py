import torch


def model(inside, params, deposit):
    return (inside + params * deposit) / (torch.sum(inside) + deposit)


def loss(p, phat):
    return torch.sum((p - phat) ** 2)


def train(p, deposit, inside, iterations, learning_rate):
    """
    Finds a set of parameters that minimize given loss function while
    fullfilling the condition of parameter non-negativity and normality
    (sum of parameter vector is 1)

    p               = desired theoretical tensor of parameters
    deposit         = amount of money to be divided between stocks
    inside          = tensor of current stock values
    learning_rate   = gradient descent step size
    """
    params = torch.rand(inside.shape[0], requires_grad=True)

    for iteration in range(1, iterations + 1):
        if params.grad is not None:
            params.grad.zero_()

        phat = model(inside, params, deposit)
        l = loss(p, phat)

        l.backward()

        params = (params - learning_rate * params.grad).detach()

        params = torch.relu(params)
        params = (params / torch.sum(params)).requires_grad_()

    return params


def exact(inside, deposit, proportions):
    return (proportions * (sum(inside) + deposit) - inside) / deposit


def calculate(percentages, deposit, current_values):
    if sum(percentages) != 1.0:
        return 'Percentages don not equal to 1'
    p = torch.tensor(percentages)
    S = deposit
    x = torch.tensor(current_values)
    return train(p, S, x, 2000, 1).tolist()
